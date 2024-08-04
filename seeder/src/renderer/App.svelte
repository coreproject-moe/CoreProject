<script lang="ts">
  import { Router, Route, Link } from 'svelte-routing'
  import Staffs from './routes/staffs/Index.svelte'
</script>

<Router>
  <h1 class="text-3xl font-semibold text-blue-500">core seeder</h1>
  <Link to="/">Home</Link>
  <Link to="/staffs">Staffs</Link>
  <div>
    <Route path="/">Home route</Route>
    <Route path="/staffs" component={Staffs} />
  </div>
</Router>
