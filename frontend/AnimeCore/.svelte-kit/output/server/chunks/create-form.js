import { createForm as createForm$1 } from "@felte/core";
import { w as writable } from "./index.js";
import { o as onDestroy } from "./ssr.js";
function __rest(s, e) {
  var t = {};
  for (var p in s)
    if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
      t[p] = s[p];
  if (s != null && typeof Object.getOwnPropertySymbols === "function")
    for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
      if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
        t[p[i]] = s[p[i]];
    }
  return t;
}
function createForm(config) {
  const _a = createForm$1(config !== null && config !== void 0 ? config : {}, {
    storeFactory: writable
  }), { cleanup, startStores } = _a, rest = __rest(_a, ["cleanup", "startStores"]);
  onDestroy(cleanup);
  return rest;
}
export {
  createForm as c
};
