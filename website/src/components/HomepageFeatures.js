import React from "react"
import clsx from "clsx"
import styles from "./HomepageFeatures.module.css"

const FeatureList = [
	{
		title: "100 Projects with Python",
		Svg: require("../../static/img/undraw_projects.svg").default,
		link: "/docs/welcome",
		description: (
			<>
				100 Python projects involving GUIs, websites, web apps, data
				science, machine learning, games, modern frameworks, and more.
			</>
		),
	},
	{
		title: "Website Built with Docusaurus",
		Svg: require("../../static/img/undraw_docusaurus_react.svg").default,
		link: "https://docusaurus.io/",
		description: (
			<>
				An optimized showcase website built with Docusaurus, providing a
				React framework with easy-to-use Markdown/MDX documentation and
				website customizability.
			</>
		),
	},
	{
		title: "Instant README Collection with FastAPI",
		Svg: require("../../static/img/undraw_fast.svg").default,
		link: "https://fastapi.tiangolo.com/",
		description: (
			<>
				An optimized FastAPI framework running on a Uvicorn ASGI server
				continuously deployed with all project READMEs for website
				display and with READMEs scraped from their project folders on
				GitHub.
			</>
		),
	},
]

function Feature({ Svg, title, description, link }) {
	return (
		<div className={clsx("col col--4")}>
			<a href={link}>
				<div className="text--center">
					<Svg className={styles.featureSvg} alt={title} />
				</div>
			</a>
			<div className="text--center padding-horiz--md">
				<h3>{title}</h3>
				<p>{description}</p>
			</div>
		</div>
	)
}

export default function HomepageFeatures() {
	return (
		<section className={styles.features}>
			<div className="container">
				<div className="row">
					{FeatureList.map((props, idx) => (
						<Feature key={idx} {...props} />
					))}
				</div>
			</div>
		</section>
	)
}
