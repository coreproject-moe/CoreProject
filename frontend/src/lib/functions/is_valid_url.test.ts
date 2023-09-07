import { is_valid_url } from "$functions/is_valid_url";
import { test, expect } from "vitest";

test("test valid url", () => {
    const https_google = "https://google.com";
    expect(is_valid_url(https_google)).toBe(true);

    const exotic_web_archive_link = `https://web.archive.org/web/20170817095211/https://github.com/Microsoft/vscode/issues/32405`;
    expect(is_valid_url(exotic_web_archive_link)).toBe(true);

    const wikipedia_link = `https://en.m.wikipedia.org/wiki/C_Sharp_(programming_language)`;
    expect(is_valid_url(wikipedia_link)).toBe(true);

    const wikipedia_link_2 = `https://zh.wikipedia.org/wiki/Wikipedia:%E5%85%B3%E4%BA%8E%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91/en`;
    expect(is_valid_url(wikipedia_link_2)).toBe(true);

    const exotic_firebase_app = `https://test-test-test-test-test-test-test-test-test.web.app/`;
    expect(is_valid_url(exotic_firebase_app)).toBe(true);

    const medium_link = `https://medium.com/@gordon_zhu/how-to-be-great-at-asking-questions-e37be04d0603`;
    expect(is_valid_url(medium_link)).toBe(true);

    // This is a interesting one
    const edge_case_domain = `http:www.example.com/main.html`;
    expect(is_valid_url(edge_case_domain)).toBe(true);

    const invalid_url = `www.example.com`;
    expect(is_valid_url(invalid_url)).toBe(false);

    const javascript_void = `javascript:void(0)`;
    expect(is_valid_url(javascript_void)).toBe(false);
});
