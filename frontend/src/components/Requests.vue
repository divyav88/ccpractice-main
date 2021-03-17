<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Requests</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.request-modal>Add Request</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Request Name</th>
              <th scope="col">Description</th>
              <th scope="col">Status</th>
              <th scope="col">Created By</th>
              <th scope="col">Updated?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(request, index) in requests" :key="index">
              <!-- <td>{{ request.requestid }}</td> -->
              <td>{{ request.name }}</td>
              <td>{{ request.description }}</td>
              <td>{{ request.status }}</td>
              <td>{{ request.createdby }}</td>             
              <td>
                <span v-if="request.updated">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.request-update-modal
                          @click="editRequest(request)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteRequest(request)">
                      Delete
                  </button>
                  <button
                          type="button"
                          class="btn btn-primary btn-sm"
                          v-b-modal.request-upload-modal
                          @click="uploadRequest(request)">
                      Uplaod
                  </button>
                  <button
                          type="button"
                          class="btn btn-info btn-sm"                         
                          @click="editRequest(request)">
                      Download
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addRequestModal"
            id="request-modal"
            title="Add a new request"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addRequestForm.name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addRequestForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-status-group"
                      label="Status:"
                      label-for="form-status-input">
            <b-form-input id="form-status-input"
                          type="text"
                          v-model="addRequestForm.status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
           <b-form-group id="form-createdby-group"
                      label="Created By:"
                      label-for="form-createdby-input">
            <b-form-input id="form-createdby-input"
                          type="text"
                          v-model="addRequestForm.createdby"
                          required
                          placeholder="Enter Created By">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-updated-group">
          <b-form-checkbox-group v-model="addRequestForm.updated" id="form-checks">
            <b-form-checkbox value="true">Updated?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editRequestModal"
            id="request-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-name-edit-group"
                    label="Name:"
                    label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-edit-group"
                      label="Description:"
                      label-for="form-description-edit-input">
            <b-form-input id="form-description-edit-input"
                          type="text"
                          v-model="editForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-status-edit-group"
                      label="Status:"
                      label-for="form-status-edit-input">
            <b-form-input id="form-status-edit-input"
                          type="text"
                          v-model="editForm.status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-createdby-edit-group"
                      label="Created By:"
                      label-for="form-createdby-edit-input">
            <b-form-input id="form-createdby-edit-input"
                          type="text"
                          v-model="editForm.createdby"
                          required
                          placeholder="Enter Created By">
            </b-form-input>
          </b-form-group>
        <!-- <b-form-group id="form-updated-edit-group">
          <b-form-checkbox-group v-model="editForm.updated" id="form-checks"> -->
            <b-form-checkbox checked="true">Updated?</b-form-checkbox>
          <!-- </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="uploadRequestModal"
            id="request-upload-modal"
            title="Upload"
            hide-footer>
        <b-form @submit.prevent="onSubmitUpload" class="w-100">          
          <b-form-file v-model="uploadedFile" class="mt-3" plain></b-form-file>
          <div class="mt-3">Selected file: {{ uploadedFile ? uploadedFile.name : '' }}</div>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      requests: [],
      addRequestForm: {
        name: '',
        description: '',
        status: '',
        createdby: '',
        updated: []
      },
      message: '',
      showMessage: false,
      editForm: {
        requestid: '',
        name: '',
        description: '',
        status: '',
        createdby: '',
        updated: []
      },
      file: '',
      uploadedFile: null
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getRequests() {
      const path = 'http://localhost:5000/requests/all';
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.get(path, optionAxios)
        .then((res) => {
          this.requests = res.data;          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addRequest(payload) {
      const path = 'http://localhost:5000/requests/add';
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.post(path, payload, optionAxios)
        .then(() => {
          console.log(`Print payload: ${payload}`)
          this.getRequests();
          this.message = 'Request added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(`Post Req Error: ${error}`);
          this.getRequests();
        });
    },
    initForm() {
      this.addRequestForm.name = '';
      this.addRequestForm.description = '';
      this.addRequestForm.status = '';
      this.addRequestForm.createdby = '';
      this.addRequestForm.updated = [];    
      
      this.editForm.requestid = '';
      this.editForm.name = '';
      this.editForm.description = '';
      this.editForm.status = '';
      this.editForm.createdby = '';
      this.editForm.updated = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addRequestModal.hide();
      let updated = false;
      if (this.addRequestForm.updated[0]) updated = true;
      const payload = {
        name: this.addRequestForm.name,
        description: this.addRequestForm.description,
        status: this.addRequestForm.status,
        createdby: this.addRequestForm.createdby,
        updated, // property shorthand
      };
      console.log(payload)
      this.addRequest(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addRequestModal.hide();
      this.initForm();
    },
    uploadRequest(request) {
      this.editForm = request;
    },
    onSubmitUpload() {   
      this.$refs.uploadRequestModal.hide();   
      console.log(this.uploadedFile)
      let requestID = this.editForm.requestid;
      let formData = new FormData();
      formData.append('image', this.uploadedFile);
       for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token'),
               'Content-Type': 'multipart/form-data'
            }
        }
      const path = `http://localhost:5000/requests/upload/${requestID}`;      
      axios.post(path, formData, optionAxios)     
          .then(() => {
            this.getRequests();
            this.message = 'File uploaded!';
            this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          // this.getRequests();
        });
    },    
    editRequest(request) {
      this.editForm = request;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRequestModal.hide();
      let updated = true;
      if (this.editForm.updated[0]) updated = true;
      const payload = {
        name: this.editForm.name,
        description: this.editForm.description,
        status: this.editForm.status,
        createdby: this.editForm.createdby,
        updated, // property shorthand
      };
      this.updateRequest(payload, this.editForm.requestid);
    },
    updateRequest(payload, requestID) {
      const path = `http://localhost:5000/requests/${requestID}`;
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.put(path, payload, optionAxios)
        .then(() => {
          this.getRequests();
          this.message = 'Request updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRequestModel.hide();
      this.initForm();
      this.getRequests(); // why?
    },
    removeRequest(requestID) {
      const path = `http://localhost:5000/requests/${requestID}`;
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.delete(path, optionAxios)
        .then(() => {
          this.getRequests();
          this.message = 'Request removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onDeleteRequest(request) {
      console.log(request)
      this.removeRequest(request.requestid);
    },
  },
  created() {
    this.getRequests();
  },
};
</script>
