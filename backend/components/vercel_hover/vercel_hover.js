(() => {
    let hover_glider_element = document.querySelector('active_glider'),
        glider_container_element = document.querySelector('glider-container'),
        direction = glider_container_element.getAttribute('direction'),
        GLIDER_TRANSITION_DURATION =
        parseInt(glider_container_element.getAttribute('duration')) || 200,
    mouse_leave_timeout = null,
    is_hovered_from_prev_el = false; // Check if hover is from previous element ( not from outside )

    /** vercel effect */
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

        glider_container_element.style.zIndex = String(target_zindex ?? 0);
        hover_glider_element.style.zIndex = String(target_zindex - 1 ?? -1);

        switch (direction) {
            case 'vertical':
                hover_glider_element.style.transform = `translateY(${target.offsetTop}px)`;
                break;
            case 'horizontal':
                hover_glider_element.style.transform = `translateX(${target.offsetLeft}px)`;
                break;
        }

        if (is_hovered_from_prev_el) {
            GLIDER_TRANSITION_DURATION = 200;
            hover_glider_element.style.transitionDuration = `${GLIDER_TRANSITION_DURATION}ms`;
        } else {
            GLIDER_TRANSITION_DURATION = 50;
            hover_glider_element.style.transitionDuration = `${GLIDER_TRANSITION_DURATION}ms`;
                // Show element after it reach its position
            setTimeout(
                () => (hover_glider_element.style.opacity = '100'),
                GLIDER_TRANSITION_DURATION
            );
            is_hovered_from_prev_el = true;
        }

        clearTimeout(mouse_leave_timeout);
    },
          handle_mouseleave = () => {
            // Delay the mouseleave event to allow time ( GLIDER_TRANSITION_DURATION ) for moving to a sibling element
        mouse_leave_timeout = setTimeout(() => {
            hover_glider_element.style.opacity = '0';
            is_hovered_from_prev_el = false;
        }, GLIDER_TRANSITION_DURATION);
    };

    Array.from(glider_container_element.children)
        .slice(1) // Remove first element
        .forEach((children) => {
            children.addEventListener('mouseenter', handle_mouseenter);
            children.addEventListener('mouseleave', handle_mouseleave);
        });
})();
