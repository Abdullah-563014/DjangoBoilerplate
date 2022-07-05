/** @type {import('tailwindcss').Config} */
module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false, //true for production build
    content: [
      '../**/views/*.html',
      '../**/views/*.html'
    ]
  },
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}
