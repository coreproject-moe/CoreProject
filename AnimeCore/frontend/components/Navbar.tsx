import Image from 'next/image';

export const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="container">
                <div className="navbar-brand">
                    <a className="navbar-item">
                        <Image
                            src="/animecore_logo.svg"
                            width={164}
                            height={25}
                        />
                    </a>
                    <span
                        className="navbar-burger"
                        data-target="navbarMenuHeroA"
                    >
                        <span></span>
                        <span></span>
                        <span></span>
                    </span>
                </div>
                <div id="navbarMenuHeroA" className="navbar-menu">
                    <div className="navbar-end">
                        <span className="navbar-item">
                            <a className="button is-ghost px-0">
                                <img
                                    src="/icons/search.svg"
                                    width={36}
                                    height={36}
                                />
                            </a>
                        </span>
                        <span className="navbar-item px-0">
                            <img
                                className="pt-2"
                                style={{ maxHeight: '100%' }}
                                src="/images/placeholder.png"
                                width={60}
                                height={60}
                            />
                        </span>
                    </div>
                </div>
            </div>
        </nav>
    );
};
