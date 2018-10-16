<template>
  <div id="twitter-feed">
    <a
      class="twitter-timeline"
      data-theme="light"
      href="https://twitter.com/FrederictonFC?ref_src=twsrc%5Etfw">
    </a>
  </div>
  <!-- data-height="400" -->
</template>

<script>
export default {
  name: 'TwitterFeed',
  mounted() {
    /* eslint-disable */
    !function(d,s,id){
      var js,fjs=d.getElementsByTagName(s)[0];
      if(!d.getElementById(id) || true){
        js=d.createElement(s);
        js.id=id;
        js.src='https://platform.twitter.com/widgets.js';
        fjs.parentNode.insertBefore(js,fjs);
      }
    }(document,'script','twitter-wjs');
    /* eslint-enable */
  },
};
</script>
