/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          orange: '#F97316',
          orangeHover: '#EA580C',
          amber: '#F59E0B',
          slate: '#0F172A',
          surface: '#F8FAFC'
        }
      },
      fontFamily: {
        sans: ['Vazirmatn', 'Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}