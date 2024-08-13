import { BaseDatabase } from "./_base";

export class StaffDatabase extends BaseDatabase {
	#table_name = "Staff";

	constructor() {
		super();
	}

	public create_table = async () => {
		this.migration_queue.push(
			this.db.prepare(`
			CREATE TABLE IF NOT EXISTS ${this.#table_name}(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				mal_id INTEGER NOT NULL,
				name TEXT,
				staff_image BLOB,
				given_name TEXT,
				alternate_name JSON,
				birthday DATETIME,
				about TEXT
			)`)
		);
	};

	public get_all_staff_given_mal_id = () => {
		const stmt = this.db.prepare(`SELECT mal_id FROM ${this.#table_name}`);
		const rows = stmt.all();
		return rows.map((row) => (row as { mal_id: number }).mal_id);
	};

	public get_staff = (id: number) => {
		const staff = this.db.prepare(`SELECT * FROM ${this.#table_name} WHERE id = ?`).get(id);
		return staff;
	};
	public get_all_null_staff = () => {
		const stmt = this.db.prepare(`
			SELECT * FROM ${this.#table_name} WHERE
				name IS NULL OR
				staff_image IS NULL OR
				given_name IS NULL OR
				alternate_name IS NULL OR
				birthday IS NULL OR
				about IS NULL
            `);
		const rows = stmt.all();
		return rows;
	};

	public create_staff = ({
		mal_id,
		name,
		given_name,
		staff_image,
		alternate_name,
		birthday,
		about
	}: {
		mal_id: number;
		name?: string;
		given_name?: string;
		staff_image?: string;
		alternate_name?: string[];
		birthday?: Date;
		about?: string;
	}) => {
		const stmt = this.db.prepare(`
			INSERT INTO ${this.#table_name} (mal_id,name, staff_image, given_name, alternate_name, birthday, about)
			VALUES (?, ?, ?, ?, ?, ?, ?)
		`);
		const alternate_name_json = alternate_name ? JSON.stringify(alternate_name) : null;
		stmt.run(
			mal_id,
			name ?? null,
			staff_image ?? null,
			given_name ?? null,
			alternate_name_json,
			birthday ?? null,
			about ?? null
		);
	};
}
