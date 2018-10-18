<template>
  <div id="modal-wrapper">
    <div id="modal-container">
      <i
        id="close-button"
        class="el-icon-circle-close"
        @click="closeModal">
      </i>
      <ModalLogin v-if="loginModalVisible"/>
      <ModalCreateAccount v-else-if="createAccoundModalVisible"/>
      <div id="modal-container-footer">
        Forgot your password?
        <span
          id="reset-password-link"
          @click="resetPasswordClick">
          <u>Reset it!</u>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ModalLogin from '@/components/ModalLogin.vue';
import ModalCreateAccount from '@/components/ModalCreateAccount.vue';

export default{
  name: 'ModalWrapper',
  components: {
    ModalLogin,
    ModalCreateAccount,
  },
  computed: {
    ...mapGetters([
      'loginModalVisible',
      'createAccoundModalVisible',
    ]),
  },
  methods: {
    ...mapActions([
      'closeModal',
    ]),
    resetPasswordClick() {
      this.$router.push('reset');
      this.closeModal();
    },
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-wrapper{
  position: fixed;
  z-index: 99;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
  display: flex;
  justify-content: center;
  align-items: center;

  #modal-container{
    width: 350px;
    display: flex;
    flex-direction: column;
    background-color: $SECONDARY_COLOR;
    border-radius: 4px;
    animation: createBox .25s;
    max-height: 100%;
    overflow-y: auto;

    #close-button{
      align-self: flex-end;
      margin-right: 4px;
      margin-top: 4px;
      font-size: 1.2rem;

      &:hover{
        cursor: pointer;
        color: #636363;
      }
    }

    #modal-container-footer{
      margin-top: 12px;
      padding-top: 8px;
      padding-bottom: 8px;
      background-color: #e8eaed;
      border-radius: 0px 0px 4px 4px;

      #reset-password-link{
        &:hover{
          cursor: pointer;
        }
      }
    }
  }

  @keyframes createBox {
    from {
      transform: scale(0);
    }
    to {
      transform: scale(1);
    }
  }
}
</style>
