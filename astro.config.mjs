// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightVersions from 'starlight-versions';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Live Production Exchange',
			plugins: [
				starlightVersions({
					current: {
						label: 'Latest - 2.0',
					},
					versions: [
						{ slug: '1.0', label: 'v1.0 (dpp)' },
					],
				}),
			],
			customCss: ['./src/styles/custom.css'],
			components: {
				Footer: './src/components/Footer.astro',
			},
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/live-production-exchange' }],
			sidebar: [
				{
					label: 'LPX 2.0',
					items: [{ slug: 'coming-soon' }]
				},
			],
		}),
	],
});
