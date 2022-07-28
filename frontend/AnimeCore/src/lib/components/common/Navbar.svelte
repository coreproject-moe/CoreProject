<script lang="ts">
    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
</script>

<div class="navbar bg-transparent">
    <div class="navbar-start hidden md:block">
        <Search height={30} width={30} />
    </div>
    <div class="navbar-center">
        <Logo variant="black" width={158} height={22} />
    </div>
    <div class="navbar-end">
        <img
            alt=""
            class="mask mask-squircle"
            src="/images/(Avatar)-placeholder.png"
            width="50"
            height="50"
        />
    </div>
</div>
