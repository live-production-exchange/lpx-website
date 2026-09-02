// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Live Production Exchange',
			customCss: ['./src/styles/custom.css'],
			components: {
				Footer: './src/components/Footer.astro',
			},
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/live-production-exchange' }],
			sidebar: [
				{
					label: 'Introduction',
					items: [{ autogenerate: { directory: 'introduction' } }]
				},
				{
					label: 'LPX Metadata',
					items: [{ autogenerate: { directory: 'schema' } }]
				},
				{
					label: 'Examples',
					items: [{ autogenerate: { directory: 'examples' } }]
				},
				{
					label: 'Reference APIs',
					items: [{ autogenerate: { directory: 'api' } }]
				},
				{
					label: 'About LPX',
					items: [{ autogenerate: { directory: 'about' } }]
				},
			],
		}),
	],
});
