import BetterSqlite3 from "better-sqlite3";

export class BaseDatabase {
	protected migration_queue: any[] = [];
	protected db: BetterSqlite3.Database;

	constructor(db: BetterSqlite3.Database) {
		this.db = db;
	}

	// Method to execute all queued migrations
	public async migrate() {
		for (const migration of this.migration_queue) {
			migration.run();
		}
	}
}
