import { Autocomplete, AutocompleteProps, Loader } from '@mantine/core';
import { useRef, useState } from 'react';

interface IProps
    extends Omit<
        AutocompleteProps,
        'data' | 'value' | 'onChange' | 'rightSection'
    > {}

const AutoComplete = (props: IProps) => {
    /** Handle Search inputs */
    /** Copied from https://ui.mantine.dev/component/autocomplete-loading */

    const timeoutRef = useRef<number>(-1);
    const [value, setValue] = useState('');
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState<string[]>([]);

    const handleSearchInput = (value: string) => {
        window.clearTimeout(timeoutRef.current);
        setValue(value);
        setData([]);

        if (value.trim().length === 0) {
            setLoading(false);
        } else {
            setLoading(true);
            timeoutRef.current = window.setTimeout(() => {
                setLoading(false);
                setData(
                    ['gmail.com', 'outlook.com', 'yahoo.com'].map(
                        (provider) => `${value}@${provider}`
                    )
                );
            }, 1000);
        }
    };
    return (
        <Autocomplete
            {...props}
            value={value}
            data={data}
            onChange={handleSearchInput}
            rightSection={loading ? <Loader size={16} /> : null}
        />
    );
};
export default AutoComplete;
