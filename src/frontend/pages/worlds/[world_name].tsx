import { GetStaticPaths, GetStaticProps } from "next";
import { getWorldData } from "../../lib/worlds";
import Layout from "../../components/layout";
import Head from "next/head";
import { getAllPostIds, getPostData } from "../../lib/posts";
import utilStyles from "../../styles/utils.module.css";
import Date from "../../components/date";

export default function World({
  worldData,
}: {
  worldData: {
    title: string;
    date: string;
    contentHtml: string;
  };
}) {
  return (
    <Layout>
      <Head>
        <title>{worldData.title}</title>
      </Head>
      <article>
        <h1 className={utilStyles.headingXl}>{worldData.title}</h1>
        <div className={utilStyles.lightText}>
          <Date dateString={worldData.date} />
        </div>
        <div dangerouslySetInnerHTML={{ __html: worldData.contentHtml }} />
      </article>
    </Layout>
  );
}

export const getStaticPaths: GetStaticPaths = async () => {
  const ids = getAllPostIds();
  // rename id to world_name
  const paths = ids.map((p) => {
    return {
      params: {
        world_name: p.params.id,
      },
    };
  });
  return {
    paths,
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const worldData = await getPostData(params?.world_name as string);
  return {
    props: {
      worldData,
    },
  };
};
