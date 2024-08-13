// https://gist.github.com/maximilian-lindsey/a446a7ee87838a62099d

import express from "express";
import cors from "cors";

const app = express();
app.use(cors());

app.get("/", (_, res) => {
	res.send("Hello World!");
});

export { app };
