import BetterSqlite3 from "better-sqlite3";

import Database from "better-sqlite3";

export class BaseDatabase {
	protected migration_queue: any[] = [];
	protected db: BetterSqlite3.Database;

	constructor() {
		this.db = new Database("seeder.db");
		this.db.pragma("journal_mode = WAL");
	}

	// Method to execute all queued migrations
	public async migrate() {
		for (const migration of this.migration_queue) {
			migration.run();
		}
	}
}
