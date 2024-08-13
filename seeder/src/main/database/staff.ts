import BetterSqlite3 from "better-sqlite3";
import { BaseDatabase } from "./_base";

export class StaffDatabase extends BaseDatabase {
	constructor(db: BetterSqlite3.Database) {
		super(db);
	}

	public create_table = async () => {
		this.migration_queue.push(
			this.db.prepare(`
			CREATE TABLE IF NOT EXISTS Staff(
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
		const stmt = this.db.prepare("SELECT mal_id FROM Staff");
		const rows = stmt.all();
		return rows.map((row) => (row as { mal_id: number }).mal_id);
	};

	public get_staff = (id: number) => {
		const staff = this.db.prepare("SELECT * FROM Staff WHERE id = ?").get(id);
		return staff;
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
			INSERT INTO Staff (mal_id,name, staff_image, given_name, alternate_name, birthday, about)
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
