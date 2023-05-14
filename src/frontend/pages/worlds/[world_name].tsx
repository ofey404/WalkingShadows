import { GetStaticPaths, GetStaticProps } from "next";
import { getWorldData } from "../../lib/worlds";
import Layout from "../../components/layout";
import Head from "next/head";
import { getAllPostIds, getPostData } from "../../lib/posts";
import utilStyles from "../../styles/utils.module.css";
import Date from "../../components/date";
import { useRouter } from "next/router";

export default function World() {
  const router = useRouter();
  const callAPI = async () => {
    try {
      const url =
        process.env.NEXT_PUBLIC_BACKEND_API +
        "/world/" +
        router.query.world_name +
        "/get";
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
      });
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
        <title>Test Title</title>
      </Head>
      <article>
        <button onClick={callAPI}>Make API call</button>
      </article>
    </Layout>
  );
}
