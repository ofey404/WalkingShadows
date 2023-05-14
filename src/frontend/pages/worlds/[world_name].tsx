import { GetStaticPaths, GetStaticProps } from "next";
import { getWorldData } from "../../lib/worlds";
import Layout from "../../components/layout";
import Head from "next/head";
import { getAllPostIds, getPostData } from "../../lib/posts";
import utilStyles from "../../styles/utils.module.css";
import Date from "../../components/date";
import { useRouter } from "next/router";

export default function World({
  worldData,
}: {
  worldData: {
    title: string;
    date: string;
    contentHtml: string;
  };
}) {
  const router = useRouter();
  const callAPI = async () => {
    try {
      const res = await fetch(`https://jsonplaceholder.typicode.com/posts/1`);
      const data = await res.json();
      console.log(data);
      console.log(process.env.NEXT_PUBLIC_BACKEND_API);
      console.log(router.query.world_name);
    } catch (err) {
      console.log(err);
    }
  };

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
        <button onClick={callAPI}>Make API call</button>
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
