import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/UltraGene/__docusaurus/debug',
    component: ComponentCreator('/UltraGene/__docusaurus/debug', '31b'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/config',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/config', 'c9d'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/content',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/content', '040'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/globalData',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/globalData', '034'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/metadata',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/metadata', 'fde'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/registry',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/registry', '3e0'),
    exact: true
  },
  {
    path: '/UltraGene/__docusaurus/debug/routes',
    component: ComponentCreator('/UltraGene/__docusaurus/debug/routes', '955'),
    exact: true
  },
  {
    path: '/UltraGene/blog',
    component: ComponentCreator('/UltraGene/blog', '173'),
    exact: true
  },
  {
    path: '/UltraGene/blog/archive',
    component: ComponentCreator('/UltraGene/blog/archive', '2ee'),
    exact: true
  },
  {
    path: '/UltraGene/blog/first-blog-post',
    component: ComponentCreator('/UltraGene/blog/first-blog-post', '3f5'),
    exact: true
  },
  {
    path: '/UltraGene/blog/long-blog-post',
    component: ComponentCreator('/UltraGene/blog/long-blog-post', '0ba'),
    exact: true
  },
  {
    path: '/UltraGene/blog/mdx-blog-post',
    component: ComponentCreator('/UltraGene/blog/mdx-blog-post', '4da'),
    exact: true
  },
  {
    path: '/UltraGene/blog/tags',
    component: ComponentCreator('/UltraGene/blog/tags', '7e2'),
    exact: true
  },
  {
    path: '/UltraGene/blog/tags/docusaurus',
    component: ComponentCreator('/UltraGene/blog/tags/docusaurus', 'b19'),
    exact: true
  },
  {
    path: '/UltraGene/blog/tags/facebook',
    component: ComponentCreator('/UltraGene/blog/tags/facebook', 'd6a'),
    exact: true
  },
  {
    path: '/UltraGene/blog/tags/hello',
    component: ComponentCreator('/UltraGene/blog/tags/hello', 'c63'),
    exact: true
  },
  {
    path: '/UltraGene/blog/tags/hola',
    component: ComponentCreator('/UltraGene/blog/tags/hola', 'af4'),
    exact: true
  },
  {
    path: '/UltraGene/blog/welcome',
    component: ComponentCreator('/UltraGene/blog/welcome', '1ea'),
    exact: true
  },
  {
    path: '/UltraGene/markdown-page',
    component: ComponentCreator('/UltraGene/markdown-page', '92e'),
    exact: true
  },
  {
    path: '/UltraGene/docs',
    component: ComponentCreator('/UltraGene/docs', '987'),
    routes: [
      {
        path: '/UltraGene/docs',
        component: ComponentCreator('/UltraGene/docs', 'b3d'),
        routes: [
          {
            path: '/UltraGene/docs',
            component: ComponentCreator('/UltraGene/docs', 'f40'),
            routes: [
              {
                path: '/UltraGene/docs/category/tutorial---basics',
                component: ComponentCreator('/UltraGene/docs/category/tutorial---basics', '65f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/intro',
                component: ComponentCreator('/UltraGene/docs/intro', '114'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/intro copy',
                component: ComponentCreator('/UltraGene/docs/intro copy', '924'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/congratulations',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/congratulations', '5e3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/create-a-blog-post',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/create-a-blog-post', 'c3e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/create-a-document',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/create-a-document', 'fbd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/create-a-page',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/create-a-page', '643'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/deploy-your-site',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/deploy-your-site', '7dc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/UltraGene/docs/tutorial-basics/markdown-features',
                component: ComponentCreator('/UltraGene/docs/tutorial-basics/markdown-features', 'd2a'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/UltraGene/',
    component: ComponentCreator('/UltraGene/', 'e95'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
