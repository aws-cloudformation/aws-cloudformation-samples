// This is a generated file. Modifications will be overwritten.
import { BaseModel, Dict, integer, Integer, Optional, transformValue } from 'cfn-rpdk';
import { Exclude, Expose, Type, Transform } from 'class-transformer';

export class ResourceModel extends BaseModel {
    ['constructor']: typeof ResourceModel;

    @Exclude()
    public static readonly TYPE_NAME: string = 'AWSSamples::Devtools::Devinstance';

    @Exclude()
    protected readonly IDENTIFIER_KEY_UID: string = '/properties/UID';

    @Expose({ name: 'UID' })
    @Transform(
        ({ value, key, obj, type }) =>
            transformValue(String, 'UID', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    UID?: Optional<string>;
    @Expose({ name: 'InstanceType' })
    @Transform(
        ({ value, key, obj, type }) =>
            transformValue(String, 'InstanceType', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    InstanceType?: Optional<string>;
    @Expose({ name: 'DiskSize' })
    @Transform(
        ({ value, key, obj, type }) =>
            transformValue(Integer, 'DiskSize', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    DiskSize?: Optional<integer>;
    @Expose({ name: 'Keypair' })
    @Transform(
        ({ value, key, obj, type }) =>
            transformValue(String, 'Keypair', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    Keypair?: Optional<string>;
    @Expose({ name: 'SSH' })
    @Transform(
        ({ value, key, obj, type }) =>
            transformValue(String, 'SSH', value, obj, []),
        {
            toClassOnly: true,
        }
    )
    SSH?: Optional<string>;

    @Exclude()
    public getPrimaryIdentifier(): Dict {
        const identifier: Dict = {};
        if (this.UID != null) {
            identifier[this.IDENTIFIER_KEY_UID] = this.UID;
        }

        // only return the identifier if it can be used, i.e. if all components are present
        return Object.keys(identifier).length === 1 ? identifier : null;
    }

    @Exclude()
    public getAdditionalIdentifiers(): Array<Dict> {
        const identifiers: Array<Dict> = new Array<Dict>();
        // only return the identifiers if any can be used
        return identifiers.length === 0 ? null : identifiers;
    }
}

