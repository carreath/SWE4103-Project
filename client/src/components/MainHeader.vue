<template>
  <div id="main-header">
    <div id="main-header-title">
      Fredericton <br>Football Club
    </div>
  </div>
</template>

<script>
export default{
  name: 'MainHeader',
  data() {
    return {

    };
  },
  components: {

  },
  props: {

  },
  computed: {

  },
  methods: {

  },
  mounted() {

  },
};
</script>

<style lang='scss' scoped>
#main-header{
  height: 180px;
  width: 100%;
  background: linear-gradient(#0c64f2, #347ed8);
  padding: 8px 8px;
  display: flex;
  justify-content: space-between;

  #main-header-title{
    color: white;
    text-align: start;
    align-self: flex-end;
    font-weight: bold;
    font-size: 48px;
  }
}
</style>
