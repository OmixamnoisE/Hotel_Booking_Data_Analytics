/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}', // Adjust this path based on where your templates are
    './admin_app/templates/**/*.{html,js}', // For templates in admin_app
    './user_app/templates/**/*.{html,js}', // For templates in user_app
    './cashier_app/templates/**/*.{html,js}' // For templates in cashier_app
  ],
  purge: ['./templates/**/*.html'],
  theme: {
    extend: {},
  },
  plugins: [],
}
