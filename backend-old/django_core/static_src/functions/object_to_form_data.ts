export async function object_to_form_data(object: object) {
    // Code from
    // https://bobbyhadz.com/blog/javascript-convert-object-to-formdata
    const form_data = new FormData();

    Object.entries(object).forEach(([key, val]) => {
        form_data.append(key, val);
    });

    return form_data;
}
