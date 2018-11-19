<template>
  <div id="modal-edit-user">
    <div id="edit-user-modal-container">
      <div id="title">
        Edit User
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          :model="userEditForm"
          :rules="userEditFormRules"
          label-width="120px"
          ref="user-edit-form">
          <el-form-item
            label="First Name"
            class = "label"
            prop="firstName">
            <el-input
              id="first-name-input"
              placeholder="First Name"
              v-model="userEditForm.firstName"
              :disabled="loading">
            </el-input>
          </el-form-item>

          <el-form-item
            label="Last Name"
            class = "label"
            prop="lastName">
            <el-input
              id="last-name-input"
              placeholder="Last Name"
              v-model="userEditForm.lastName"
              :disabled="loading">
            </el-input>
          </el-form-item>

          <el-form-item
            label="Email"
            class = "label"
            prop="email">
            <el-input
              id="email-input"
              type="email"
              placeholder="Email"
              v-model="userEditForm.email"
              :disabled="loading">
            </el-input>
          </el-form-item>

          <el-form-item
            label="User Type"
            class = "label"
            prop="userType">
            <el-select
              v-model="userEditForm.userType"
              id="user-type-input"
              :style="{'float': 'left'}"
              placeholder="User type">
              <el-option label="Admin" value="Admin"></el-option>
              <el-option label="Coordinator" value="Coordinator"></el-option>
              <el-option label="Manager" value="Manager"></el-option>
              <el-option label="Referee" value="Referee"></el-option>
              <el-option label="None" :value="null"></el-option>
            </el-select>
          </el-form-item>

          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
        </el-form>
      </div>
      <div class="footer">
        <el-button
          :loading="loading"
          @click="userEditButtonClicked">
          Cancel
        </el-button>
        <div></div>
        <el-button
          type="primary"
          :loading="loading"
          @click="closeModal">
          {{ userEditButtonText }}
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ModalEditUser',
  data() {
    return {
      labelPosition: 'left',
      userEditForm: {
        firstName: '',
        lastName: '',
        email: '',
        userType: '',
      },
      userEditFormRules: {
        firstName: [
          {
            required: true,
            message: 'Please input first name.',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 32,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please input last name.',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 32,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        email: [
          {
            required: true,
            message: 'Please input email',
            trigger: 'blur',
          },
          {
            type: 'email',
            message: 'Please input correct email address',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        userType: [
          {
            required: true,
            message: 'Please input user type',
            trigger: 'blur',
          },
        ],
      },
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    ...mapGetters([
      'editUserModalVisible',
      'editedUser',
      'editedUserId',
    ]),
    userEditButtonText() {
      return this.loading ? 'Loading' : 'Edit User';
    },
  },
  methods: {
    ...mapActions([
      'closeModal',
      'editUser',
    ]),
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.closeModal();
      }
      // Enter key
      if (e.keyCode === 13) {
        this.userEditButtonClicked();
      }
    },
    userEditButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['user-edit-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.editUser(this.userEditForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.closeModal();
            } else {
              this.errMsg = response.retMsg;
            }
          });
        }
      });
    },
  },
  mounted() {
    this.userEditForm = { ...this.editedUser };
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#modal-edit-user{
  #edit-user-modal-container{
    padding: 0px 40px;
    display: flex;
    flex-direction: column;

    #title{
      font-size: 2rem;
      font-weight: bold;
      margin-bottom: 8px;
    }

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
    }

    #first-name-input,
    #last-name-input,
    #email-input{
      margin: 8px 0px;
    }

    #user-type-input{
      margin: 8px 0px;
      display: block;

      .el-select{
        display: block;
      }
    }

    #errMsg{
      color: red;
    }

    #user-edit-button-container{
      width: 100%;
      margin: 8px 0px;

      button{
        width: 50%;
      }
    }

    .footer{
      display: flex;
      justify-content: space-between;
      margin-bottom: 12px;
    }
  }
}
</style>
