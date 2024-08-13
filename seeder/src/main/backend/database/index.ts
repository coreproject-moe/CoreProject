import BetterSqlite3 from "better-sqlite3";

class InternalDatabase {
	#db: BetterSqlite3.Database;

	constructor(db: BetterSqlite3.Database) {
		this.#db = db;
	}

	public migrate = async () => {
		const staff_data = this.#db.prepare(`
            CREATE TABLE IF NOT EXISTS Staff(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mal_id INTEGER,
                name TEXT,
                staff_image TEXT,
                given_name TEXT,
                alternate_name JSON,
                birthday DATETIME,
                about TEXT
            )    
        `);

		staff_data.run();
	};
}

export { InternalDatabase as Database };
