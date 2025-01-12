import { StaffDatabase } from "./staff";

class InternalDatabase extends StaffDatabase {
	constructor() {
		super();
	}
}

export { InternalDatabase as Database };
