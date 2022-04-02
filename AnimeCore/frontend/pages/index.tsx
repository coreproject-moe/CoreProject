import Image from 'next/image';
import type { NextPage } from 'next';
import { Navbar } from '../components/Navbar';

const Home: NextPage = () => {
    return (
        <>
            <section
                className="hero is-fullheight has-background-black"
                style={{
                    backgroundImage: `url(${'/images/Hyouka-poster.png'})`,
                    backgroundRepeat: 'no-repeat',
                    backgroundPosition: 'center',
                    backgroundSize: 'cover',
                    boxShadow: `
                        inset 0 4px 1800px #070519,
                        inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
                        inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
                        inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
                        inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)
                    `,
                }}
            >
                <div className="hero-head">
                    <Navbar />
                </div>

                <div className="hero-body is-align-items-self-end">
                    <div className="container">
                        <div className="title has-text-warning is-size-4">
                            Featured <span className="is-bold">——</span>
                        </div>
                        <div className="title is-size-1 has-text-white is-bold">
                            Hyouka
                        </div>
                        <div
                            className="subtitle is-size-6 has-text-white pt-5"
                            style={{
                                width: '60%',
                            }}
                        >
                            Energy-conservative high school student Houtarou
                            Oreki ends up with more than he bargained for when
                            he signs up for the Classic Literature Club at his
                            sister's behest—especially when he realizes how
                            deep-rooted the club's history really is.
                            Begrudgingly, Oreki is dragged into an...
                        </div>
                        <div className="subtitle">
                            <span className="tag is-size-6 mx-1 is-bold is-black">
                                Mystery
                            </span>
                            <span className="tag is-size-6 mx-1 is-bold is-black">
                                Slice of Life
                            </span>
                        </div>
                        <div className="subtitle">
                            <div className="buttons">
                                <button
                                    className="button is-warning has-border-transparent mx-3"
                                    style={{
                                        borderRadius: 12,
                                    }}
                                >
                                    <span className="icon is-small">
                                        <Image
                                            src="/icons/play.svg"
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                </button>
                                <button
                                    className="button is-warning is-outlined"
                                    style={{
                                        borderRadius: 16,
                                        borderWidth: 3,
                                    }}
                                >
                                    <span className="is-bold">Detailes</span>
                                    <Image
                                        src="/icons/chevrons-right.svg"
                                        height={24}
                                        width={24}
                                    />
                                </button>
                                <button
                                    className="button is-warning is-outlined"
                                    style={{
                                        borderRadius: 16,
                                        borderWidth: 3,
                                    }}
                                >
                                    <span className="icon is-small">
                                        <Image
                                            src="/icons/chevron-left.svg"
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                </button>
                                <button
                                    className="button is-warning is-outlined"
                                    style={{
                                        borderRadius: 16,
                                        borderWidth: 3,
                                    }}
                                >
                                    <span className="icon is-small">
                                        <Image
                                            src="/icons/chevron-right.svg"
                                            height={24}
                                            width={24}
                                        />
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="hero-foot">
                    <nav className="tabs">
                        <div className="container has-text-white">
                            <div className="columns is-mobile is-centered">
                                <div className="column is-narrow px-1">
                                    <Image
                                        src="/icons/arrow-down.svg"
                                        height={24}
                                        width={24}
                                    />
                                </div>
                                <div className="column is-narrow px-1">
                                    scroll below
                                </div>
                            </div>
                        </div>
                    </nav>
                </div>
            </section>
        </>
    );
};

export default Home;
