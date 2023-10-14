(() => {
	let scroll_area = document.querySelector("scroll-area"),
		add_mask_bottom = scroll_area.scrollHeight > scroll_area.clientHeight,
		mask_class = "[mask-image:_linear-gradient(180deg,_rgba(7,5,25,0.95)_80%,_rgba(0,0,0,0)_100%)]"

	if (add_mask_bottom) scroll_area.classList.add(mask_class);

	scroll_area.addEventListener("scroll", () => {
		const { clientHeight, scrollHeight, scrollTop } = scroll_area;

		if (clientHeight + scrollTop === scrollHeight) scroll_area.classList.remove(mask_class);
		else scroll_area.classList.add(mask_class);
	});
})();