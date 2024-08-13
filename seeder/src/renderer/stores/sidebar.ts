import { createRoot, createSignal } from "solid-js";

function createSidebarStore() {
  const [open, setOpen] = createSignal(false);
  return { open, setOpen }
}

export default createRoot(createSidebarStore);
