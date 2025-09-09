export default {
  general: {
    browserslist: '> 0.2%, last 2 versions, Firefox ESR, not dead and fully supports loading-lazy-attr', // defaults = '> 0.5%, last 2 versions, Firefox ESR, not dead'
  },
  css: {
    inline_critical_css: false,
  },
  image: {
    cdn: {
      process: 'optimize',
    },
  },
  video: {
    autoplay_lazyload: {
      when: 'never',
    }
  },
  misc: {
    prefetch_links: 'in-viewport',
  }
};