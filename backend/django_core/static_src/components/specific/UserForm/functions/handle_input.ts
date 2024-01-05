import * as z from "zod";

export function handle_input({ event, schema, error_field }: { event: Event; schema: z.Schema; error_field: { error: string[] } }) {
    const target = event.target as HTMLInputElement;

    try {
        schema.parse(target.value);
        console.log(1);
        error_field.error = new Array<string>();
    } catch (err) {
        if (err instanceof z.ZodError) {
            error_field.error = Object.values(err.flatten().formErrors) as unknown as string[];
        }
    }
}
