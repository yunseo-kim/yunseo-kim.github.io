/**
 * Setting up image lazy loading and LQIP switching
 */

const ATTR_DATA_SRC = 'data-src';
const ATTR_DATA_LQIP = 'data-lqip';

const cover = {
  SHIMMER: 'shimmer',
  BLUR: 'blur'
};

function removeCover(clzss) {
  this.parentElement.classList.remove(clzss);
}

function handleImage() {
  if (!this.complete) {
    return;
  }

  if (this.hasAttribute(ATTR_DATA_LQIP)) {
    removeCover.call(this, cover.BLUR);
  } else {
    removeCover.call(this, cover.SHIMMER);
  }
}

/**
 * Switches the LQIP with the real image URL.
 */
function switchLQIP() {
  const src = this.getAttribute(ATTR_DATA_SRC);
  this.setAttribute('src', encodeURI(src));
  this.removeAttribute(ATTR_DATA_SRC);
}

export function loadImg() {
  const images = document.querySelectorAll('article img');

  if (images.length === 0) {
    return;
  }

  images.forEach((img) => {
    img.addEventListener('load', handleImage);
  });

  // Images loaded from the browser cache do not trigger the 'load' event
  // Modified by Yunseo Kim: Images without both loading=“lazy” attribute and data-lqip attribute also do not trigger 'load' event
  document.querySelectorAll('article img').forEach((img) => {
    if (!img.hasAttribute(ATTR_DATA_LQIP) && img.complete) {
      removeCover.call(img, cover.SHIMMER);
    }
  });

  // LQIPs set by the data URI or WebP will not trigger the 'load' event,
  // so manually convert the URI to the URL of a high-resolution image.
  const lqips = document.querySelectorAll(
    `article img[${ATTR_DATA_LQIP}="true"]`
  );

  if (lqips.length) {
    lqips.forEach((lqip) => {
      switchLQIP.call(lqip);
    });
  }
}
