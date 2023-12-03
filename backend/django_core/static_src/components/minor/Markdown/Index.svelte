<script lang="ts">
    // Import scss
    import "highlight.js/scss/github-dark.scss";

    // Import js codes
    import { onMount } from "svelte";
    import { sanitize } from "$functions/sanitize";
    import { Marked } from "marked";
    import { markedEmoji } from "marked-emoji";
    import { markedHighlight } from "marked-highlight";
    import { mangle } from "marked-mangle";
    import { markedXhtml } from "marked-xhtml";
    import { markedSmartypants } from "marked-smartypants";
    import { cn } from "$functions/classname";
    import hljs from "highlight.js/lib/core";
    let marked: Marked;

    onMount(async () => {
        const emojis = (await import("../../../data/emoji.json")).default;

        marked = new Marked(
            // Highlight.js
            markedHighlight({
                langPrefix: "hljs language-",
                highlight: (code, lang) => {
                    const language = hljs.getLanguage(lang) ? lang : "plaintext";
                    return hljs.highlight(code, { language }).value;
                }
            }),
            // Emoji plugin
            markedEmoji({
                emojis,
                unicode: false
            }),
            {
                extensions: [
                    {
                        name: "emoji",
                        renderer: (token) => {
                            return `<img class="inline-flex w-4 justify-center align-center -translate-y-0.5 md:w-[1vw]" alt="${token.name}" src="${token.emoji}">`;
                        }
                    }
                ]
            },
            // Smartypants plugin
            markedSmartypants(),
            // XHTML plugin
            markedXhtml(),
            // Mangle plugin
            mangle(),
            // Marked defaults
            {
                gfm: true
            }
        );
        hljs.registerLanguage("1c", (await import("highlight.js/lib/languages/1c")).default);
        hljs.registerLanguage("abnf", (await import("highlight.js/lib/languages/abnf")).default);
        hljs.registerLanguage("accesslog", (await import("highlight.js/lib/languages/accesslog")).default);
        hljs.registerLanguage("actionscript", (await import("highlight.js/lib/languages/actionscript")).default);
        hljs.registerLanguage("ada", (await import("highlight.js/lib/languages/ada")).default);
        hljs.registerLanguage("angelscript", (await import("highlight.js/lib/languages/angelscript")).default);
        hljs.registerLanguage("apache", (await import("highlight.js/lib/languages/apache")).default);
        hljs.registerLanguage("applescript", (await import("highlight.js/lib/languages/applescript")).default);
        hljs.registerLanguage("arcade", (await import("highlight.js/lib/languages/arcade")).default);
        hljs.registerLanguage("arduino", (await import("highlight.js/lib/languages/arduino")).default);
        hljs.registerLanguage("armasm", (await import("highlight.js/lib/languages/armasm")).default);
        hljs.registerLanguage("xml", (await import("highlight.js/lib/languages/xml")).default);
        hljs.registerLanguage("asciidoc", (await import("highlight.js/lib/languages/asciidoc")).default);
        hljs.registerLanguage("aspectj", (await import("highlight.js/lib/languages/aspectj")).default);
        hljs.registerLanguage("autohotkey", (await import("highlight.js/lib/languages/autohotkey")).default);
        hljs.registerLanguage("autoit", (await import("highlight.js/lib/languages/autoit")).default);
        hljs.registerLanguage("avrasm", (await import("highlight.js/lib/languages/avrasm")).default);
        hljs.registerLanguage("awk", (await import("highlight.js/lib/languages/awk")).default);
        hljs.registerLanguage("axapta", (await import("highlight.js/lib/languages/axapta")).default);
        hljs.registerLanguage("bash", (await import("highlight.js/lib/languages/bash")).default);
        hljs.registerLanguage("basic", (await import("highlight.js/lib/languages/basic")).default);
        hljs.registerLanguage("bnf", (await import("highlight.js/lib/languages/bnf")).default);
        hljs.registerLanguage("brainfuck", (await import("highlight.js/lib/languages/brainfuck")).default);
        hljs.registerLanguage("c", (await import("highlight.js/lib/languages/c")).default);
        hljs.registerLanguage("cal", (await import("highlight.js/lib/languages/cal")).default);
        hljs.registerLanguage("capnproto", (await import("highlight.js/lib/languages/capnproto")).default);
        hljs.registerLanguage("ceylon", (await import("highlight.js/lib/languages/ceylon")).default);
        hljs.registerLanguage("clean", (await import("highlight.js/lib/languages/clean")).default);
        hljs.registerLanguage("clojure", (await import("highlight.js/lib/languages/clojure")).default);
        hljs.registerLanguage("clojure-repl", (await import("highlight.js/lib/languages/clojure-repl")).default);
        hljs.registerLanguage("cmake", (await import("highlight.js/lib/languages/cmake")).default);
        hljs.registerLanguage("coffeescript", (await import("highlight.js/lib/languages/coffeescript")).default);
        hljs.registerLanguage("coq", (await import("highlight.js/lib/languages/coq")).default);
        hljs.registerLanguage("cos", (await import("highlight.js/lib/languages/cos")).default);
        hljs.registerLanguage("cpp", (await import("highlight.js/lib/languages/cpp")).default);
        hljs.registerLanguage("crmsh", (await import("highlight.js/lib/languages/crmsh")).default);
        hljs.registerLanguage("crystal", (await import("highlight.js/lib/languages/crystal")).default);
        hljs.registerLanguage("csharp", (await import("highlight.js/lib/languages/csharp")).default);
        hljs.registerLanguage("csp", (await import("highlight.js/lib/languages/csp")).default);
        hljs.registerLanguage("css", (await import("highlight.js/lib/languages/css")).default);
        hljs.registerLanguage("d", (await import("highlight.js/lib/languages/d")).default);
        hljs.registerLanguage("markdown", (await import("highlight.js/lib/languages/markdown")).default);
        hljs.registerLanguage("dart", (await import("highlight.js/lib/languages/dart")).default);
        hljs.registerLanguage("delphi", (await import("highlight.js/lib/languages/delphi")).default);
        hljs.registerLanguage("diff", (await import("highlight.js/lib/languages/diff")).default);
        hljs.registerLanguage("django", (await import("highlight.js/lib/languages/django")).default);
        hljs.registerLanguage("dns", (await import("highlight.js/lib/languages/dns")).default);
        hljs.registerLanguage("dockerfile", (await import("highlight.js/lib/languages/dockerfile")).default);
        hljs.registerLanguage("dos", (await import("highlight.js/lib/languages/dos")).default);
        hljs.registerLanguage("dsconfig", (await import("highlight.js/lib/languages/dsconfig")).default);
        hljs.registerLanguage("dts", (await import("highlight.js/lib/languages/dts")).default);
        hljs.registerLanguage("dust", (await import("highlight.js/lib/languages/dust")).default);
        hljs.registerLanguage("ebnf", (await import("highlight.js/lib/languages/ebnf")).default);
        hljs.registerLanguage("elixir", (await import("highlight.js/lib/languages/elixir")).default);
        hljs.registerLanguage("elm", (await import("highlight.js/lib/languages/elm")).default);
        hljs.registerLanguage("ruby", (await import("highlight.js/lib/languages/ruby")).default);
        hljs.registerLanguage("erb", (await import("highlight.js/lib/languages/erb")).default);
        hljs.registerLanguage("erlang-repl", (await import("highlight.js/lib/languages/erlang-repl")).default);
        hljs.registerLanguage("erlang", (await import("highlight.js/lib/languages/erlang")).default);
        hljs.registerLanguage("excel", (await import("highlight.js/lib/languages/excel")).default);
        hljs.registerLanguage("fix", (await import("highlight.js/lib/languages/fix")).default);
        hljs.registerLanguage("flix", (await import("highlight.js/lib/languages/flix")).default);
        hljs.registerLanguage("fortran", (await import("highlight.js/lib/languages/fortran")).default);
        hljs.registerLanguage("fsharp", (await import("highlight.js/lib/languages/fsharp")).default);
        hljs.registerLanguage("gams", (await import("highlight.js/lib/languages/gams")).default);
        hljs.registerLanguage("gauss", (await import("highlight.js/lib/languages/gauss")).default);
        hljs.registerLanguage("gcode", (await import("highlight.js/lib/languages/gcode")).default);
        hljs.registerLanguage("gherkin", (await import("highlight.js/lib/languages/gherkin")).default);
        hljs.registerLanguage("glsl", (await import("highlight.js/lib/languages/glsl")).default);
        hljs.registerLanguage("gml", (await import("highlight.js/lib/languages/gml")).default);
        hljs.registerLanguage("go", (await import("highlight.js/lib/languages/go")).default);
        hljs.registerLanguage("golo", (await import("highlight.js/lib/languages/golo")).default);
        hljs.registerLanguage("gradle", (await import("highlight.js/lib/languages/gradle")).default);
        hljs.registerLanguage("graphql", (await import("highlight.js/lib/languages/graphql")).default);
        hljs.registerLanguage("groovy", (await import("highlight.js/lib/languages/groovy")).default);
        hljs.registerLanguage("haml", (await import("highlight.js/lib/languages/haml")).default);
        hljs.registerLanguage("handlebars", (await import("highlight.js/lib/languages/handlebars")).default);
        hljs.registerLanguage("haskell", (await import("highlight.js/lib/languages/haskell")).default);
        hljs.registerLanguage("haxe", (await import("highlight.js/lib/languages/haxe")).default);
        hljs.registerLanguage("hsp", (await import("highlight.js/lib/languages/hsp")).default);
        hljs.registerLanguage("http", (await import("highlight.js/lib/languages/http")).default);
        hljs.registerLanguage("hy", (await import("highlight.js/lib/languages/hy")).default);
        hljs.registerLanguage("inform7", (await import("highlight.js/lib/languages/inform7")).default);
        hljs.registerLanguage("ini", (await import("highlight.js/lib/languages/ini")).default);
        hljs.registerLanguage("irpf90", (await import("highlight.js/lib/languages/irpf90")).default);
        hljs.registerLanguage("isbl", (await import("highlight.js/lib/languages/isbl")).default);
        hljs.registerLanguage("java", (await import("highlight.js/lib/languages/java")).default);
        hljs.registerLanguage("javascript", (await import("highlight.js/lib/languages/javascript")).default);
        hljs.registerLanguage("jboss-cli", (await import("highlight.js/lib/languages/jboss-cli")).default);
        hljs.registerLanguage("json", (await import("highlight.js/lib/languages/json")).default);
        hljs.registerLanguage("julia", (await import("highlight.js/lib/languages/julia")).default);
        hljs.registerLanguage("julia-repl", (await import("highlight.js/lib/languages/julia-repl")).default);
        hljs.registerLanguage("kotlin", (await import("highlight.js/lib/languages/kotlin")).default);
        hljs.registerLanguage("lasso", (await import("highlight.js/lib/languages/lasso")).default);
        hljs.registerLanguage("latex", (await import("highlight.js/lib/languages/latex")).default);
        hljs.registerLanguage("ldif", (await import("highlight.js/lib/languages/ldif")).default);
        hljs.registerLanguage("leaf", (await import("highlight.js/lib/languages/leaf")).default);
        hljs.registerLanguage("less", (await import("highlight.js/lib/languages/less")).default);
        hljs.registerLanguage("lisp", (await import("highlight.js/lib/languages/lisp")).default);
        hljs.registerLanguage("livecodeserver", (await import("highlight.js/lib/languages/livecodeserver")).default);
        hljs.registerLanguage("livescript", (await import("highlight.js/lib/languages/livescript")).default);
        hljs.registerLanguage("llvm", (await import("highlight.js/lib/languages/llvm")).default);
        hljs.registerLanguage("lsl", (await import("highlight.js/lib/languages/lsl")).default);
        hljs.registerLanguage("lua", (await import("highlight.js/lib/languages/lua")).default);
        hljs.registerLanguage("makefile", (await import("highlight.js/lib/languages/makefile")).default);
        hljs.registerLanguage("mathematica", (await import("highlight.js/lib/languages/mathematica")).default);
        hljs.registerLanguage("matlab", (await import("highlight.js/lib/languages/matlab")).default);
        hljs.registerLanguage("maxima", (await import("highlight.js/lib/languages/maxima")).default);
        hljs.registerLanguage("mel", (await import("highlight.js/lib/languages/mel")).default);
        hljs.registerLanguage("mercury", (await import("highlight.js/lib/languages/mercury")).default);
        hljs.registerLanguage("mipsasm", (await import("highlight.js/lib/languages/mipsasm")).default);
        hljs.registerLanguage("mizar", (await import("highlight.js/lib/languages/mizar")).default);
        hljs.registerLanguage("perl", (await import("highlight.js/lib/languages/perl")).default);
        hljs.registerLanguage("mojolicious", (await import("highlight.js/lib/languages/mojolicious")).default);
        hljs.registerLanguage("monkey", (await import("highlight.js/lib/languages/monkey")).default);
        hljs.registerLanguage("moonscript", (await import("highlight.js/lib/languages/moonscript")).default);
        hljs.registerLanguage("n1ql", (await import("highlight.js/lib/languages/n1ql")).default);
        hljs.registerLanguage("nestedtext", (await import("highlight.js/lib/languages/nestedtext")).default);
        hljs.registerLanguage("nginx", (await import("highlight.js/lib/languages/nginx")).default);
        hljs.registerLanguage("nim", (await import("highlight.js/lib/languages/nim")).default);
        hljs.registerLanguage("nix", (await import("highlight.js/lib/languages/nix")).default);
        hljs.registerLanguage("node-repl", (await import("highlight.js/lib/languages/node-repl")).default);
        hljs.registerLanguage("nsis", (await import("highlight.js/lib/languages/nsis")).default);
        hljs.registerLanguage("objectivec", (await import("highlight.js/lib/languages/objectivec")).default);
        hljs.registerLanguage("ocaml", (await import("highlight.js/lib/languages/ocaml")).default);
        hljs.registerLanguage("openscad", (await import("highlight.js/lib/languages/openscad")).default);
        hljs.registerLanguage("oxygene", (await import("highlight.js/lib/languages/oxygene")).default);
        hljs.registerLanguage("parser3", (await import("highlight.js/lib/languages/parser3")).default);
        hljs.registerLanguage("pf", (await import("highlight.js/lib/languages/pf")).default);
        hljs.registerLanguage("pgsql", (await import("highlight.js/lib/languages/pgsql")).default);
        hljs.registerLanguage("php", (await import("highlight.js/lib/languages/php")).default);
        hljs.registerLanguage("php-template", (await import("highlight.js/lib/languages/php-template")).default);
        hljs.registerLanguage("plaintext", (await import("highlight.js/lib/languages/plaintext")).default);
        hljs.registerLanguage("pony", (await import("highlight.js/lib/languages/pony")).default);
        hljs.registerLanguage("powershell", (await import("highlight.js/lib/languages/powershell")).default);
        hljs.registerLanguage("processing", (await import("highlight.js/lib/languages/processing")).default);
        hljs.registerLanguage("profile", (await import("highlight.js/lib/languages/profile")).default);
        hljs.registerLanguage("prolog", (await import("highlight.js/lib/languages/prolog")).default);
        hljs.registerLanguage("properties", (await import("highlight.js/lib/languages/properties")).default);
        hljs.registerLanguage("protobuf", (await import("highlight.js/lib/languages/protobuf")).default);
        hljs.registerLanguage("puppet", (await import("highlight.js/lib/languages/puppet")).default);
        hljs.registerLanguage("purebasic", (await import("highlight.js/lib/languages/purebasic")).default);
        hljs.registerLanguage("python", (await import("highlight.js/lib/languages/python")).default);
        hljs.registerLanguage("python-repl", (await import("highlight.js/lib/languages/python-repl")).default);
        hljs.registerLanguage("q", (await import("highlight.js/lib/languages/q")).default);
        hljs.registerLanguage("qml", (await import("highlight.js/lib/languages/qml")).default);
        hljs.registerLanguage("r", (await import("highlight.js/lib/languages/r")).default);
        hljs.registerLanguage("reasonml", (await import("highlight.js/lib/languages/reasonml")).default);
        hljs.registerLanguage("rib", (await import("highlight.js/lib/languages/rib")).default);
        hljs.registerLanguage("roboconf", (await import("highlight.js/lib/languages/roboconf")).default);
        hljs.registerLanguage("routeros", (await import("highlight.js/lib/languages/routeros")).default);
        hljs.registerLanguage("rsl", (await import("highlight.js/lib/languages/rsl")).default);
        hljs.registerLanguage("ruleslanguage", (await import("highlight.js/lib/languages/ruleslanguage")).default);
        hljs.registerLanguage("rust", (await import("highlight.js/lib/languages/rust")).default);
        hljs.registerLanguage("sas", (await import("highlight.js/lib/languages/sas")).default);
        hljs.registerLanguage("scala", (await import("highlight.js/lib/languages/scala")).default);
        hljs.registerLanguage("scheme", (await import("highlight.js/lib/languages/scheme")).default);
        hljs.registerLanguage("scilab", (await import("highlight.js/lib/languages/scilab")).default);
        hljs.registerLanguage("scss", (await import("highlight.js/lib/languages/scss")).default);
        hljs.registerLanguage("shell", (await import("highlight.js/lib/languages/shell")).default);
        hljs.registerLanguage("smali", (await import("highlight.js/lib/languages/smali")).default);
        hljs.registerLanguage("smalltalk", (await import("highlight.js/lib/languages/smalltalk")).default);
        hljs.registerLanguage("sml", (await import("highlight.js/lib/languages/sml")).default);
        hljs.registerLanguage("sqf", (await import("highlight.js/lib/languages/sqf")).default);
        hljs.registerLanguage("sql", (await import("highlight.js/lib/languages/sql")).default);
        hljs.registerLanguage("stan", (await import("highlight.js/lib/languages/stan")).default);
        hljs.registerLanguage("stata", (await import("highlight.js/lib/languages/stata")).default);
        hljs.registerLanguage("step21", (await import("highlight.js/lib/languages/step21")).default);
        hljs.registerLanguage("stylus", (await import("highlight.js/lib/languages/stylus")).default);
        hljs.registerLanguage("subunit", (await import("highlight.js/lib/languages/subunit")).default);
        hljs.registerLanguage("swift", (await import("highlight.js/lib/languages/swift")).default);
        hljs.registerLanguage("taggerscript", (await import("highlight.js/lib/languages/taggerscript")).default);
        hljs.registerLanguage("yaml", (await import("highlight.js/lib/languages/yaml")).default);
        hljs.registerLanguage("tap", (await import("highlight.js/lib/languages/tap")).default);
        hljs.registerLanguage("tcl", (await import("highlight.js/lib/languages/tcl")).default);
        hljs.registerLanguage("thrift", (await import("highlight.js/lib/languages/thrift")).default);
        hljs.registerLanguage("tp", (await import("highlight.js/lib/languages/tp")).default);
        hljs.registerLanguage("twig", (await import("highlight.js/lib/languages/twig")).default);
        hljs.registerLanguage("typescript", (await import("highlight.js/lib/languages/typescript")).default);
        hljs.registerLanguage("vala", (await import("highlight.js/lib/languages/vala")).default);
        hljs.registerLanguage("vbnet", (await import("highlight.js/lib/languages/vbnet")).default);
        hljs.registerLanguage("vbscript", (await import("highlight.js/lib/languages/vbscript")).default);
        hljs.registerLanguage("vbscript-html", (await import("highlight.js/lib/languages/vbscript-html")).default);
        hljs.registerLanguage("verilog", (await import("highlight.js/lib/languages/verilog")).default);
        hljs.registerLanguage("vhdl", (await import("highlight.js/lib/languages/vhdl")).default);
        hljs.registerLanguage("vim", (await import("highlight.js/lib/languages/vim")).default);
        hljs.registerLanguage("wasm", (await import("highlight.js/lib/languages/wasm")).default);
        hljs.registerLanguage("wren", (await import("highlight.js/lib/languages/wren")).default);
        hljs.registerLanguage("x86asm", (await import("highlight.js/lib/languages/x86asm")).default);
        hljs.registerLanguage("xl", (await import("highlight.js/lib/languages/xl")).default);
        hljs.registerLanguage("xquery", (await import("highlight.js/lib/languages/xquery")).default);
        hljs.registerLanguage("zephir", (await import("highlight.js/lib/languages/zephir")).default);
    });

    export let markdown = "";
    let klass = "";
    export { klass as class };

    let html: string | Promise<string>;
    $: html = sanitize(marked.parse(markdown));
</script>

<div class={cn(klass)}>
    {#await html then html}
        {@html html}
    {/await}
</div>
