import { encode } from "html-entities";
class OpengraphGenerator {
  #title;
  #url;
  #description;
  #site_name;
  #locale;
  #audio;
  #image;
  #video;
  #keywords;
  constructor({
    title,
    url,
    description,
    site_name,
    locale,
    audio,
    image_url,
    video,
    keywords
  }) {
    this.#title = encode(title);
    this.#url = url;
    this.#description = encode(description);
    this.#site_name = site_name;
    this.#locale = locale;
    if (audio) {
      this.#audio = audio;
    }
    if (image_url) {
      this.#image = image_url;
    }
    if (video) {
      this.#video = video;
    }
    if (keywords) {
      this.#keywords = keywords;
    }
  }
  get title() {
    let title = `<title>${this.#title}</title>`;
    title += `<meta property="og:title" content="${this.#title}">`;
    title += `<meta name="twitter:title" content="${this.#title}" />`;
    return title;
  }
  get url() {
    return `<meta property="og:url" content="${this.#url}">`;
  }
  get description() {
    let description = `<meta name="description" content="${this.#description}">`;
    description += `<meta property="og:description" content="${this.#description}">`;
    description += `<meta name="twitter:description" content="${this.#description}" />`;
    return description;
  }
  get site_name() {
    return `<meta property="og:site_name" content="${this.#site_name}">`;
  }
  get locale() {
    return `<meta property="og:locale" content="${this.#locale}">`;
  }
  get audio() {
    return `<meta property="og:audio" content="${this.#audio}">`;
  }
  get image() {
    let image = "";
    image += `<meta property="og:image" content="${this.#image}">`;
    image += `<meta name="twitter:image" content="${this.#image}" />`;
    return image;
  }
  get video() {
    let video_opengraph_text = "";
    if (this.#video?.url) {
      video_opengraph_text += `<meta property="og:video" content="${this.#video.url}">`;
    }
    if (this.#video?.title) {
      video_opengraph_text += `<meta property="og:video:title" content="${this.#video?.title}">`;
    }
    if (this.#video?.type) {
      video_opengraph_text += `<meta property="og:video:type" content="${this.#video.type}">`;
    }
    if (this.#video?.height) {
      video_opengraph_text += `<meta property="og:video:height" content="${this.#video.height}">`;
    }
    if (this.#video?.width) {
      video_opengraph_text += `<meta property="og:video:width" content="${this.#video.width}">`;
    }
    if (this.#video?.description) {
      video_opengraph_text += `<meta property="og:video:description" content="${this.#video.description}">`;
    }
    if (this.#video?.secure_url) {
      video_opengraph_text += `<meta property="og:video:secure_url" content="${this.#video.secure_url}">`;
    }
    if (this.#video?.tag) {
      video_opengraph_text += `<meta property="og:video:tag" content="Video Tag">`;
    }
    if (this.#video?.duration) {
      video_opengraph_text += `<meta property="og:video:duration" content="${this.#video.duration}">`;
    }
    if (this.#video?.release_date) {
      video_opengraph_text += `<meta property="og:video:release_date" content="${this.#video.release_date}">`;
    }
    return video_opengraph_text;
  }
  get keywords() {
    return `<meta name="keywords" content="${this.#keywords?.join(", ")}"/>`;
  }
  generate_opengraph() {
    let opengraph_html = `<meta property="og:type" content="website">`;
    opengraph_html += this.site_name;
    opengraph_html += this.locale;
    opengraph_html += this.title;
    opengraph_html += this.url;
    opengraph_html += this.description;
    if (this.#audio) {
      opengraph_html += this.audio;
    }
    if (this.#image) {
      opengraph_html += this.image;
      opengraph_html += `<meta name="twitter:card" content="summary_large_image" />`;
    }
    if (this.#video) {
      opengraph_html += this.video;
    }
    if (this.#keywords) {
      opengraph_html += this.keywords;
    }
    return opengraph_html;
  }
}
export {
  OpengraphGenerator as O
};
