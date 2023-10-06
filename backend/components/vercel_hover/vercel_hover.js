(() => {
    /** vercel effect */
    const hover_glider_element = document.querySelector('active_glider'),
        glider_container_element = document.querySelector('glider-container'),
        direction = glider_container_element.getAttribute('direction'),
        GLIDER_TRANSITION_DURATION = 200,
        is_hovered = false, // Boolean switch flag
        mouse_leave_timeout = null;

    const handle_mouseenter = (event) => {
            const target = event.target;
            const target_computed_style = getComputedStyle(target);

            // To make sure our operations are proper we need to make sure that the `position` is set to relative
            glider_container_element.style.position = 'relative';

            // Do some magic here to get the target's height and width
            // Don't change the position of this code.
            // It will cause animation jank
            hover_glider_element.style.height = target_computed_style.height;
            hover_glider_element.style.width = target_computed_style.width;

            // We need to make sure that zIndex is not auto
            const target_zindex = parseInt(target_computed_style.zIndex);
            hover_glider_element.style.zIndex = String(
                target_zindex ? target_zindex - 1 : -1
            );

            switch (direction) {
                case 'vertical':
                    hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;
                    break;
                case 'horizontal':
                    hover_glider_element.style.transform = `translateX(${target.offsetLeft}px)`;
                    break;
            }

            if (!is_hovered) {
                GLIDER_TRANSITION_DURATION = 50;
                hover_glider_element.style.opacity = '100';
                is_hovered = true;
            } else {
                GLIDER_TRANSITION_DURATION = 200;
            }

            clearTimeout(mouse_leave_timeout);
        },
        handle_mouseleave = () => {
            // Delay the mouseleave event to allow time ( GLIDER_TRANSITION_DURATION ) for moving to a sibling element
            mouse_leave_timeout = setTimeout(() => {
                hover_glider_element.style.opacity = '0';
                is_hovered = false;
            }, GLIDER_TRANSITION_DURATION);
        };

    Array.from(glider_container_element.children)
        .slice(1) // Remove first element
        .forEach((children) => {
            children.addEventListener('mouseenter', handle_mouseenter);
            children.addEventListener('mouseleave', handle_mouseleave);
        });
})();
