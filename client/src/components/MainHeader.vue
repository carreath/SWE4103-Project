<template>
  <div id="main-header">
    <div id="main-header-minor">
      <div id="login">
        Login
      </div>
      <div id="create-account">
        Create Account
      </div>
    </div>
    <div id="main-header-major">
      <div id="main-header-title">
        Fredericton <br>Football Club
      </div>
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
  height: 212px;
  width: 100%;
  display: flex;
  flex-direction: column;

  #main-header-minor{
    height: 32px;
    background-color: #fcfcfc;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-right: 8px;

    #login{
      margin: 0px 4px;
      font-weight: bold;

      &:hover{
        cursor: pointer;
        text-decoration: underline;
      }
    }

    #create-account{
      margin: 0px 4px;

      &:hover{
        cursor: pointer;
        text-decoration: underline;
      }
    }
  }

  #main-header-major{
    height: 180px;
    background: linear-gradient(#0c64f2, #347ed8);
    padding: 8px 8px;
    width: calc(100% - 16px);
    display: flex;
    justify-content: space-between;

    #main-header-title{
      color: #fcfcfc;
      text-align: start;
      align-self: flex-end;
      font-weight: bold;
      font-size: 48px;
    }
  }
}
</style>
