import BetterSqlite3 from "better-sqlite3";
import { StaffDatabase } from "./staff";

class InternalDatabase extends StaffDatabase {
	constructor(db: BetterSqlite3.Database) {
		super(db);
	}
}

export { InternalDatabase as Database };
