<template>
  <div id='login-modal'>
    <div>

    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'LoginModal',
  data() {
    return {

    };
  },
  computed: {

  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
    ]),
    closeModal(e) {
      if (e.keyCode === 27) {
        this.setLoginModalVisible(false);
      }
    },
  },
  mounted() {
    window.addEventListener('keyup', this.closeModal);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.closeModal);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#login-modal{
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}
</style>
