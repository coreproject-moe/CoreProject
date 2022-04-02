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
                        inset 0 -50vh 140px 2px rgba(7, 5, 25, 0.9),
                        inset 0 -25vh 140px 2px rgba(7, 5, 25, 0.7),
                        inset 0 -10vh 140px 2px rgba(7, 5, 25, 0.4),
                        inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.2)
                    `,
                }}
            >
                <div className="hero-head">
                    <Navbar />
                </div>

                <div className="hero-body">
                    <div className="container">
                        <div className="title has-text-yellow is-size-4">
                            Featured <span className="is-bold">——</span>
                        </div>
                        <div className="title is-size-1 has-text-white">
                            Hyouka
                        </div>
                        <div
                            className="subtitle is-size-6 has-text-white"
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
                        <span className="tag is-size-6 mx-1">Mystery</span>
                        <span className="tag is-size-6 mx-1">
                            Slice of Life
                        </span>
                    </div>
                </div>

                <div className="hero-foot">
                    <nav className="tabs">
                        <div className="container">
                            <ul>
                                <li className="is-active">
                                    <a>Overview</a>
                                </li>
                                <li>
                                    <a>Modifiers</a>
                                </li>
                                <li>
                                    <a>Grid</a>
                                </li>
                                <li>
                                    <a>Elements</a>
                                </li>
                                <li>
                                    <a>Components</a>
                                </li>
                                <li>
                                    <a>Layout</a>
                                </li>
                            </ul>
                        </div>
                    </nav>
                </div>
            </section>
        </>
    );
};

export default Home;
