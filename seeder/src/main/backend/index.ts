// https://gist.github.com/maximilian-lindsey/a446a7ee87838a62099d

import express from "express";
import cors from "cors";
import Database from "better-sqlite3";
import { Database as ORM } from "$database/index";

const db = new Database("seeder.db");
db.pragma("journal_mode = WAL");

const app = express();

const orm = new ORM(db);
orm.migrate();

app.use(cors());

app.get("/", (_, res) => {
	res.send("Hello World!");
});

app.get("/shiinobi-healthcheck", (_, res) => {
	res.send("We are friends");
});

app.get("/staff/:id", (req, res) => {
	const item = orm.get_staff(Number(req.params.id));
	res.json(item);
});

app.get("/staff/create/:id", (req, res) => {
	orm.create_staff({ mal_id: Number(req.params.id) });
	res.send("OK");
});

export { app };
