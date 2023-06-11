import React, { type ReactElement } from "react";
import Head from "next/head";
import { useRouter } from "next/router";
import Layout from "../../components/layout";

export default function World(): ReactElement {
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
