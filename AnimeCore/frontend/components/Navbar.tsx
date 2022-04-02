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
                            <a className="button is-ghost">
                                <Image
                                    src="/icons/search.svg"
                                    width={32}
                                    height={32}
                                    layout="fixed"
                                />
                            </a>
                        </span>
                        <span className="navbar-item px-0">
                            <Image
                                style={{ maxHeight: '100%' }}
                                src="/images/placeholder.png"
                                width={60}
                                height={60}
                                layout="fixed"
                            />
                        </span>
                    </div>
                </div>
            </div>
        </nav>
    );
};
