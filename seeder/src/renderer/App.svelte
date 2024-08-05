<script lang="ts">
  import { Router, Route } from 'svelte-routing'
  import Staffs from '@routes/staffs/Index.svelte'
  import HomeLayout from '@layouts/HomeLayout.svelte'
</script>

<Router>
  <HomeLayout>
    <Route path="/">Home route</Route>
    <Route path="/staffs" component={Staffs} />
  </HomeLayout>
</Router>
