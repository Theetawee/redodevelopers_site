/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
	darkMode: "class",
	theme: {
		extend: {
			colors: {
				primary: {
					50: "#fff7ed",
					100: "#ffedd5",
					200: "#fed7aa",
					300: "#fdba74",
					400: "#fb923c",
					500: "#ee6435", // Median
					600: "#ea580c", // Slightly darker
					700: "#c2410c", // Darker
					800: "#9a3412", // Even darker
					900: "#7c2d12", // Very dark
					950: "#431407", // Extremely dark
				},
			},
		},
	},
	plugins: [require("flowbite/plugin")],
};
