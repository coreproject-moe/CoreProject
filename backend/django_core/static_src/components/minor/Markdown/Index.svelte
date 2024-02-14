<script lang="ts">
    // Import scss
    import "highlight.js/scss/github-dark.scss";

    // Import js codes
    import emojis from "../../../data/emoji.json";
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

    onMount(async () => {
        const langauges = {
            "1c": (await import("highlight.js/lib/languages/1c")).default,
            abnf: (await import("highlight.js/lib/languages/abnf")).default,
            accesslog: (await import("highlight.js/lib/languages/accesslog")).default,
            actionscript: (await import("highlight.js/lib/languages/actionscript")).default,
            ada: (await import("highlight.js/lib/languages/ada")).default,
            angelscript: (await import("highlight.js/lib/languages/angelscript")).default,
            apache: (await import("highlight.js/lib/languages/apache")).default,
            applescript: (await import("highlight.js/lib/languages/applescript")).default,
            arcade: (await import("highlight.js/lib/languages/arcade")).default,
            arduino: (await import("highlight.js/lib/languages/arduino")).default,
            armasm: (await import("highlight.js/lib/languages/armasm")).default,
            xml: (await import("highlight.js/lib/languages/xml")).default,
            asciidoc: (await import("highlight.js/lib/languages/asciidoc")).default,
            aspectj: (await import("highlight.js/lib/languages/aspectj")).default,
            autohotkey: (await import("highlight.js/lib/languages/autohotkey")).default,
            autoit: (await import("highlight.js/lib/languages/autoit")).default,
            avrasm: (await import("highlight.js/lib/languages/avrasm")).default,
            awk: (await import("highlight.js/lib/languages/awk")).default,
            axapta: (await import("highlight.js/lib/languages/axapta")).default,
            bash: (await import("highlight.js/lib/languages/bash")).default,
            basic: (await import("highlight.js/lib/languages/basic")).default,
            bnf: (await import("highlight.js/lib/languages/bnf")).default,
            brainfuck: (await import("highlight.js/lib/languages/brainfuck")).default,
            c: (await import("highlight.js/lib/languages/c")).default,
            cal: (await import("highlight.js/lib/languages/cal")).default,
            capnproto: (await import("highlight.js/lib/languages/capnproto")).default,
            ceylon: (await import("highlight.js/lib/languages/ceylon")).default,
            clean: (await import("highlight.js/lib/languages/clean")).default,
            clojure: (await import("highlight.js/lib/languages/clojure")).default,
            "clojure-repl": (await import("highlight.js/lib/languages/clojure-repl")).default,
            cmake: (await import("highlight.js/lib/languages/cmake")).default,
            coffeescript: (await import("highlight.js/lib/languages/coffeescript")).default,
            coq: (await import("highlight.js/lib/languages/coq")).default,
            cos: (await import("highlight.js/lib/languages/cos")).default,
            cpp: (await import("highlight.js/lib/languages/cpp")).default,
            crmsh: (await import("highlight.js/lib/languages/crmsh")).default,
            crystal: (await import("highlight.js/lib/languages/crystal")).default,
            csharp: (await import("highlight.js/lib/languages/csharp")).default,
            csp: (await import("highlight.js/lib/languages/csp")).default,
            css: (await import("highlight.js/lib/languages/css")).default,
            d: (await import("highlight.js/lib/languages/d")).default,
            markdown: (await import("highlight.js/lib/languages/markdown")).default,
            dart: (await import("highlight.js/lib/languages/dart")).default,
            delphi: (await import("highlight.js/lib/languages/delphi")).default,
            diff: (await import("highlight.js/lib/languages/diff")).default,
            django: (await import("highlight.js/lib/languages/django")).default,
            dns: (await import("highlight.js/lib/languages/dns")).default,
            dockerfile: (await import("highlight.js/lib/languages/dockerfile")).default,
            dos: (await import("highlight.js/lib/languages/dos")).default,
            dsconfig: (await import("highlight.js/lib/languages/dsconfig")).default,
            dts: (await import("highlight.js/lib/languages/dts")).default,
            dust: (await import("highlight.js/lib/languages/dust")).default,
            ebnf: (await import("highlight.js/lib/languages/ebnf")).default,
            elixir: (await import("highlight.js/lib/languages/elixir")).default,
            elm: (await import("highlight.js/lib/languages/elm")).default,
            ruby: (await import("highlight.js/lib/languages/ruby")).default,
            erb: (await import("highlight.js/lib/languages/erb")).default,
            "erlang-repl": (await import("highlight.js/lib/languages/erlang-repl")).default,
            erlang: (await import("highlight.js/lib/languages/erlang")).default,
            excel: (await import("highlight.js/lib/languages/excel")).default,
            fix: (await import("highlight.js/lib/languages/fix")).default,
            flix: (await import("highlight.js/lib/languages/flix")).default,
            fortran: (await import("highlight.js/lib/languages/fortran")).default,
            fsharp: (await import("highlight.js/lib/languages/fsharp")).default,
            gams: (await import("highlight.js/lib/languages/gams")).default,
            gauss: (await import("highlight.js/lib/languages/gauss")).default,
            gcode: (await import("highlight.js/lib/languages/gcode")).default,
            gherkin: (await import("highlight.js/lib/languages/gherkin")).default,
            glsl: (await import("highlight.js/lib/languages/glsl")).default,
            gml: (await import("highlight.js/lib/languages/gml")).default,
            go: (await import("highlight.js/lib/languages/go")).default,
            golo: (await import("highlight.js/lib/languages/golo")).default,
            gradle: (await import("highlight.js/lib/languages/gradle")).default,
            graphql: (await import("highlight.js/lib/languages/graphql")).default,
            groovy: (await import("highlight.js/lib/languages/groovy")).default,
            haml: (await import("highlight.js/lib/languages/haml")).default,
            handlebars: (await import("highlight.js/lib/languages/handlebars")).default,
            haskell: (await import("highlight.js/lib/languages/haskell")).default,
            haxe: (await import("highlight.js/lib/languages/haxe")).default,
            hsp: (await import("highlight.js/lib/languages/hsp")).default,
            http: (await import("highlight.js/lib/languages/http")).default,
            hy: (await import("highlight.js/lib/languages/hy")).default,
            inform7: (await import("highlight.js/lib/languages/inform7")).default,
            ini: (await import("highlight.js/lib/languages/ini")).default,
            irpf90: (await import("highlight.js/lib/languages/irpf90")).default,
            isbl: (await import("highlight.js/lib/languages/isbl")).default,
            java: (await import("highlight.js/lib/languages/java")).default,
            javascript: (await import("highlight.js/lib/languages/javascript")).default,
            "jboss-cli": (await import("highlight.js/lib/languages/jboss-cli")).default,
            json: (await import("highlight.js/lib/languages/json")).default,
            julia: (await import("highlight.js/lib/languages/julia")).default,
            "julia-repl": (await import("highlight.js/lib/languages/julia-repl")).default,
            kotlin: (await import("highlight.js/lib/languages/kotlin")).default,
            lasso: (await import("highlight.js/lib/languages/lasso")).default,
            latex: (await import("highlight.js/lib/languages/latex")).default,
            ldif: (await import("highlight.js/lib/languages/ldif")).default,
            leaf: (await import("highlight.js/lib/languages/leaf")).default,
            less: (await import("highlight.js/lib/languages/less")).default,
            lisp: (await import("highlight.js/lib/languages/lisp")).default,
            livecodeserver: (await import("highlight.js/lib/languages/livecodeserver")).default,
            livescript: (await import("highlight.js/lib/languages/livescript")).default,
            llvm: (await import("highlight.js/lib/languages/llvm")).default,
            lsl: (await import("highlight.js/lib/languages/lsl")).default,
            lua: (await import("highlight.js/lib/languages/lua")).default,
            makefile: (await import("highlight.js/lib/languages/makefile")).default,
            mathematica: (await import("highlight.js/lib/languages/mathematica")).default,
            matlab: (await import("highlight.js/lib/languages/matlab")).default,
            maxima: (await import("highlight.js/lib/languages/maxima")).default,
            mel: (await import("highlight.js/lib/languages/mel")).default,
            mercury: (await import("highlight.js/lib/languages/mercury")).default,
            mipsasm: (await import("highlight.js/lib/languages/mipsasm")).default,
            mizar: (await import("highlight.js/lib/languages/mizar")).default,
            perl: (await import("highlight.js/lib/languages/perl")).default,
            mojolicious: (await import("highlight.js/lib/languages/mojolicious")).default,
            monkey: (await import("highlight.js/lib/languages/monkey")).default,
            moonscript: (await import("highlight.js/lib/languages/moonscript")).default,
            n1ql: (await import("highlight.js/lib/languages/n1ql")).default,
            nestedtext: (await import("highlight.js/lib/languages/nestedtext")).default,
            nginx: (await import("highlight.js/lib/languages/nginx")).default,
            nim: (await import("highlight.js/lib/languages/nim")).default,
            nix: (await import("highlight.js/lib/languages/nix")).default,
            "node-repl": (await import("highlight.js/lib/languages/node-repl")).default,
            nsis: (await import("highlight.js/lib/languages/nsis")).default,
            objectivec: (await import("highlight.js/lib/languages/objectivec")).default,
            ocaml: (await import("highlight.js/lib/languages/ocaml")).default,
            openscad: (await import("highlight.js/lib/languages/openscad")).default,
            oxygene: (await import("highlight.js/lib/languages/oxygene")).default,
            parser3: (await import("highlight.js/lib/languages/parser3")).default,
            pf: (await import("highlight.js/lib/languages/pf")).default,
            pgsql: (await import("highlight.js/lib/languages/pgsql")).default,
            php: (await import("highlight.js/lib/languages/php")).default,
            "php-template": (await import("highlight.js/lib/languages/php-template")).default,
            plaintext: (await import("highlight.js/lib/languages/plaintext")).default,
            pony: (await import("highlight.js/lib/languages/pony")).default,
            powershell: (await import("highlight.js/lib/languages/powershell")).default,
            processing: (await import("highlight.js/lib/languages/processing")).default,
            profile: (await import("highlight.js/lib/languages/profile")).default,
            prolog: (await import("highlight.js/lib/languages/prolog")).default,
            properties: (await import("highlight.js/lib/languages/properties")).default,
            protobuf: (await import("highlight.js/lib/languages/protobuf")).default,
            puppet: (await import("highlight.js/lib/languages/puppet")).default,
            purebasic: (await import("highlight.js/lib/languages/purebasic")).default,
            python: (await import("highlight.js/lib/languages/python")).default,
            "python-repl": (await import("highlight.js/lib/languages/python-repl")).default,
            q: (await import("highlight.js/lib/languages/q")).default,
            qml: (await import("highlight.js/lib/languages/qml")).default,
            r: (await import("highlight.js/lib/languages/r")).default,
            reasonml: (await import("highlight.js/lib/languages/reasonml")).default,
            rib: (await import("highlight.js/lib/languages/rib")).default,
            roboconf: (await import("highlight.js/lib/languages/roboconf")).default,
            routeros: (await import("highlight.js/lib/languages/routeros")).default,
            rsl: (await import("highlight.js/lib/languages/rsl")).default,
            ruleslanguage: (await import("highlight.js/lib/languages/ruleslanguage")).default,
            rust: (await import("highlight.js/lib/languages/rust")).default,
            sas: (await import("highlight.js/lib/languages/sas")).default,
            scala: (await import("highlight.js/lib/languages/scala")).default,
            scheme: (await import("highlight.js/lib/languages/scheme")).default,
            scilab: (await import("highlight.js/lib/languages/scilab")).default,
            scss: (await import("highlight.js/lib/languages/scss")).default,
            shell: (await import("highlight.js/lib/languages/shell")).default,
            smali: (await import("highlight.js/lib/languages/smali")).default,
            smalltalk: (await import("highlight.js/lib/languages/smalltalk")).default,
            sml: (await import("highlight.js/lib/languages/sml")).default,
            sqf: (await import("highlight.js/lib/languages/sqf")).default,
            sql: (await import("highlight.js/lib/languages/sql")).default,
            stan: (await import("highlight.js/lib/languages/stan")).default,
            stata: (await import("highlight.js/lib/languages/stata")).default,
            step21: (await import("highlight.js/lib/languages/step21")).default,
            stylus: (await import("highlight.js/lib/languages/stylus")).default,
            subunit: (await import("highlight.js/lib/languages/subunit")).default,
            swift: (await import("highlight.js/lib/languages/swift")).default,
            taggerscript: (await import("highlight.js/lib/languages/taggerscript")).default,
            yaml: (await import("highlight.js/lib/languages/yaml")).default,
            tap: (await import("highlight.js/lib/languages/tap")).default,
            tcl: (await import("highlight.js/lib/languages/tcl")).default,
            thrift: (await import("highlight.js/lib/languages/thrift")).default,
            tp: (await import("highlight.js/lib/languages/tp")).default,
            twig: (await import("highlight.js/lib/languages/twig")).default,
            typescript: (await import("highlight.js/lib/languages/typescript")).default,
            vala: (await import("highlight.js/lib/languages/vala")).default,
            vbnet: (await import("highlight.js/lib/languages/vbnet")).default,
            vbscript: (await import("highlight.js/lib/languages/vbscript")).default,
            "vbscript-html": (await import("highlight.js/lib/languages/vbscript-html")).default,
            verilog: (await import("highlight.js/lib/languages/verilog")).default,
            vhdl: (await import("highlight.js/lib/languages/vhdl")).default,
            vim: (await import("highlight.js/lib/languages/vim")).default,
            wasm: (await import("highlight.js/lib/languages/wasm")).default,
            wren: (await import("highlight.js/lib/languages/wren")).default,
            x86asm: (await import("highlight.js/lib/languages/x86asm")).default,
            xl: (await import("highlight.js/lib/languages/xl")).default,
            xquery: (await import("highlight.js/lib/languages/xquery")).default,
            zephir: (await import("highlight.js/lib/languages/zephir")).default
        };
        Object.entries(langauges).forEach((item) => {
            hljs.registerLanguage(item[0], item[1]);
        });
    });

    export let markdown = "";
    let klass = "";
    export { klass as class };

    const marked = new Marked(
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

    let html: string | Promise<string>;
    $: html = sanitize(marked.parse(markdown) ?? "");
</script>

<div class={cn(klass)}>
    {#await html then html}
        {@html html}
    {/await}
</div>
