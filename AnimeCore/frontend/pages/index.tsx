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
                    <div className="container has-text-centered">
                        <p className="title">Title</p>
                        <p className="subtitle">Subtitle</p>
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
