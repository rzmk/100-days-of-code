const lightCodeTheme = require("prism-react-renderer/themes/github")
const darkCodeTheme = require("prism-react-renderer/themes/okaidia")

/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
	title: "100 Days of Code",
	tagline: "By Mueez Khan",
	url: "https://100.mueezkhan.com",
	baseUrl: "/",
	onBrokenLinks: "throw",
	onBrokenMarkdownLinks: "warn",
	favicon: "img/mk-logo.ico",
	organizationName: "rzmk", // Usually your GitHub org/user name.
	projectName: "100-days-of-code", // Usually your repo name.
	themeConfig: {
		navbar: {
			title: "Mueez Khan",
			logo: {
				alt: "Mueez Khan Logo",
				src: "img/mk-logo.png",
			},
			items: [
				{
					type: "doc",
					docId: "welcome",
					position: "left",
					label: "100 Days of Code",
				},
				{
					href: "https://github.com/rzmk/100-days-of-code",
					label: "GitHub",
					position: "right",
				},
			],
		},
		footer: {
			style: "dark",
			links: [
				{
					title: "100 Days of Code",
					items: [
						{
							label: "Welcome!",
							to: "/docs/welcome",
						},
					],
				},
				{
					title: "Socials",
					items: [
						{
							label: "GitHub",
							href: "https://github.com/rzmk",
						},
						{
							label: "Linkedin",
							href: "https://linkedin.com/in/mueez-khan",
						},
						{
							label: "Twitter",
							href: "https://twitter.com/mueezkhan_",
						},
					],
				},
				{
					title: "More",
					items: [
						{
							label: "Mueez Khan",
							href: "https://www.mueezkhan.com/",
						},
						{
							label: "100 Days of Code",
							href: "https://100.mueezkhan.com/",
						},
					],
				},
			],
			copyright: `Copyright © ${new Date().getFullYear()} Mueez Khan. Built with <a href="https://docusaurus.io/">Docusaurus</a>.`,
		},
		prism: {
			theme: lightCodeTheme,
			darkTheme: darkCodeTheme,
		},
	},
	presets: [
		[
			"@docusaurus/preset-classic",
			{
				docs: {
					sidebarPath: require.resolve("./sidebars.js"),
					// Please change this to your repo.
					editUrl:
						"https://github.com/rzmk/100-days-of-code/edit/main/website/",
				},
				theme: {
					customCss: require.resolve("./src/css/custom.css"),
				},
			},
		],
	],
	plugins: [
		[
			"docusaurus-plugin-remote-content",
			{
				sourceBaseUrl: "https://rzmk-100-days-of-code.herokuapp.com/",
				documents: [
					"day-16",
					"day-17",
					"day-18",
					"day-19",
					"day-20",
					"day-21",
				],
				docsIntegration: true,
			},
		],
	],
}
