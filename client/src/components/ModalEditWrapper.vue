<template>
  <div id="modal-edit-wrapper">
    <div id="modal-container">
      <i
        id="close-button"
        class="el-icon-circle-close"
        @click="closeModalButtonClicked">
      </i>
      <ModalEditLeague v-if="editLeagueModalVisible"/>
      <ModalEditTeam v-else-if="editTeamModalVisible"/>
      <ModalEditUser v-else-if="editUserModalVisible"/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ModalEditLeague from '@/components/ModalEditLeague.vue';
import ModalEditTeam from '@/components/ModalEditTeam.vue';
import ModalEditUser from '@/components/ModalEditUser.vue';

export default{
  name: 'ModalEditWrapper',
  components: {
    ModalEditLeague,
    ModalEditTeam,
    ModalEditUser,
  },
  computed: {
    ...mapGetters([
      'editLeagueModalVisible',
      'editTeamModalVisible',
      'editUserModalVisible',
    ]),
  },
  methods: {
    ...mapActions([
      'closeModal',
      'getLeagues',
      'getTeams',
    ]),
    closeModalButtonClicked() {
      this.getLeagues();
      this.getTeams();
      // TODO get users if admin
      this.closeModal();
    },
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-edit-wrapper{
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
    width: 500px;
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
