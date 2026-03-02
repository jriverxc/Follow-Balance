/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html", "./app/**/*.py"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#eefdf9",
          100: "#d5f7ef",
          500: "#1fa97a",
          600: "#188963",
          700: "#146f52",
        },
      },
    },
  },
  plugins: [],
};
