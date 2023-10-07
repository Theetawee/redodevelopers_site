/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
	darkMode: "class",
	theme: {
		extend: {
			colors: {
				other: {
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
				primary: {
					100: "#fce0d7",
					200: "#f8c1ae",
					300: "#f5a286",
					400: "#f1835d",
					500: "#ee6435",
					600: "#be502a",
					700: "#8f3c20",
					800: "#5f2815",
					900: "#30140b",
				},
			},
		},
	},
	plugins: [require("flowbite/plugin")],
};
